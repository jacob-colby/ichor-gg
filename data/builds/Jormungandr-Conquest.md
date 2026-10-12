---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.3
  aspect_win_rate: 0.61
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.39
    win_rate: 0.58
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.68
    - name: Eye of Erebus
      pick_rate: 0.14
      win_rate: 0.57
  - name: Sun Beam Bow
    pick_rate: 0.14
    win_rate: 0.64
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.12
      win_rate: 0.68
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.65
  - name: Ethereal Staff
    pick_rate: 0.11
    win_rate: 0.56
    alternates:
    - name: Gladiator's Shield
      pick_rate: 0.09
      win_rate: 0.69
    - name: Sanguine Lash
      pick_rate: 0.07
      win_rate: 0.73
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.63
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.09
      win_rate: 0.85
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.64
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.47
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.4
  - name: Medallion
    pick_rate: 0.04
    win_rate: 0.75
    alternates:
    - name: Manchu Bow
      pick_rate: 0.04
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.04
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.27
    win_rate: 0.55
  - name: Sundering Axe
    pick_rate: 0.16
    win_rate: 0.72
  - name: Bluestone Pendant
    pick_rate: 0.12
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-10-12'
  god_win_rate: 0.5974025974025974
  god_matches_won: 92
  god_matches_played: 154
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-12'
  god_matches_analyzed: 6672
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Kinetic Cuirass, Shield Splitter, Genji''s Guard, Breastplate of Valor, Golden
    Blade, Runeforged Hammer, Eye of the Storm, Erosion, Pharaoh''s Curse, Eye of
    Providence, Lernaean Bow, Draconic Scale, Shogun''s Ofuda, Hydra''s Lament, Shield
    of the Phoenix, Stone of Binding, Tyrfing, Nimble Ring, Helm of Radiance, Gluttonous
    Grimoire, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Screeching Gargoyle,
    Midgardian Mail, Bragi''s Harp, Tekko-Kagi, Daybreak Gavel, Spear of Desolation,
    Heartseeker, Rod of Asclepius, Leviathan''s Hide, Void Shield, Stampede, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.64
      pick: 0.12
      fit: 0.58
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.68
      pick: 0.18
      fit: 0.48
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.53
      win: 0.85
      pick: 0.15
      fit: 0.25
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - Silverbranch Bow
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Shifter's Shield
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge,
    Shield of the Phoenix, Kinetic Cuirass, Rod of Asclepius, Golden Blade, Soul Gem,
    Runeforged Hammer, Genji''s Guard, Breastplate of Valor, Shield Splitter, Eye
    of the Storm, Pharaoh''s Curse, The Reaper, Yogi''s Necklace, Lernaean Bow, Erosion,
    Shogun''s Ofuda, Hydra''s Lament, Gluttonous Grimoire, Eye of Providence, Phoenix
    Feather, Tyrfing, Chandra''s Grace, Riptalon, Draconic Scale, Nimble Ring, Avenging
    Blade, Lifebinder, Helm of Radiance, Stone of Binding, Glorious Pridwen, Daybreak
    Gavel, Midgardian Mail, Bragi''s Harp, Tekko-Kagi, Sphere of Negation.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.49
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.32
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.53
      win: 0.64
      pick: 0.0
      fit: 0.71
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.68
      pick: 0.18
      fit: 0.46
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.53
      win: 0.85
      pick: 0.15
      fit: 0.26
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.76
  community_ordered:
  - Shifter's Shield
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield, Amanita Charm,
    Stone of Binding, Kinetic Cuirass, Avenging Blade, Screeching Gargoyle, Gluttonous
    Grimoire, Genji''s Guard, Void Shield, Breastplate of Valor, Spear of Desolation,
    Spear of the Magus, Void Stone, Heartseeker, Shield Splitter, Soul Gem, Tekko-Kagi,
    Obsidian Shard, Runeforged Hammer, Golden Blade, Toxic Blade, Titan''s Bane, The
    Crusher, Eye of the Storm, Hydra''s Lament, Lernaean Bow, Erosion, Nimble Ring,
    Pharaoh''s Curse, The Reaper, Helm of Radiance, Eye of Providence, Shield of the
    Phoenix, Draconic Scale, Doom Orb, Shogun''s Ofuda, Tyrfing.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.51
      win: 0.64
      pick: 0.0
      fit: 0.66
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.47
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.68
      pick: 0.18
      fit: 0.37
    Silverbranch Bow:
      total: 0.64
      efficiency: 0.53
      win: 0.85
      pick: 0.15
      fit: 0.42
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Shifter's Shield
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Shifter's Shield
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Kinetic Cuirass, Nimble Ring, Golden Blade, Gluttonous Grimoire, Genji''s Guard,
    Breastplate of Valor, Tyrfing, Shield Splitter, Runeforged Hammer, Soul Gem, Pharaoh''s
    Curse, Riptalon, Lernaean Bow, Shogun''s Ofuda, Erosion, Helm of Radiance, Eye
    of Providence, Stone of Binding, Eye of the Storm, Shield of the Phoenix, Hydra''s
    Lament, Toxic Blade, Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak
    Gavel, The Reaper, Spear of Desolation, Spear of the Magus, Bragi''s Harp, Midgardian
    Mail, Mantle Of Discord, Tekko-Kagi, Rod of Asclepius, Avenging Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.3
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.68
      pick: 0.18
      fit: 0.37
    Silverbranch Bow:
      total: 0.63
      efficiency: 0.53
      win: 0.85
      pick: 0.15
      fit: 0.36
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Shifter's Shield
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Silverbranch Bow
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Genji''s Guard, Breastplate of Valor, Amanita Charm, Kinetic
    Cuirass, Shield of the Phoenix, Gladiator''s Shield, Spear of Desolation, Hydra''s
    Lament, Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Shield Splitter, Nimble
    Ring, Runeforged Hammer, Helm of Radiance, Gluttonous Grimoire, Erosion, Pharaoh''s
    Curse, Golden Blade, Eye of Providence, Stone of Binding, Draconic Scale, Shogun''s
    Ofuda, Eye of the Storm, Arondight, Gem of Focus, Lernaean Bow, Spear of the Magus,
    Magi''s Cloak, Rod of Asclepius, Daybreak Gavel, Mantle Of Discord, Obsidian Shard,
    Midgardian Mail, Tyrfing, Eye of Erebus.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.64
      pick: 0.0
      fit: 0.41
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.63
      pick: 0.27
      fit: 0.55
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.53
      win: 0.85
      pick: 0.15
      fit: 0.2
  community_ordered:
  - Freya's Tears
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Genji''s
    Guard, Breastplate of Valor, Eye of the Storm, Gluttonous Grimoire, Golden Blade,
    Hydra''s Lament, Heartseeker, Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi,
    Eye of Providence, Spear of the Magus, Avenging Blade, Shield of the Phoenix,
    Stone of Binding, Draconic Scale, Helm of Radiance, Tyrfing, Titan''s Bane, Soul
    Gem, The Crusher, Obsidian Shard, Pharaoh''s Curse, Magi''s Cloak, The Reaper,
    Nimble Ring, Shogun''s Ofuda, Screeching Gargoyle, Mantle Of Discord, Midgardian
    Mail, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.64
      pick: 0.12
      fit: 0.52
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.68
      pick: 0.18
      fit: 0.42
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.53
      win: 0.85
      pick: 0.15
      fit: 0.27
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Freya's Tears
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Genji''s
    Guard, Breastplate of Valor, Shield Splitter, Spear of the Magus, Spear of Desolation,
    Nimble Ring, Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian Shard, Golden
    Blade, Eye of the Storm, Hydra''s Lament, Lernaean Bow, Rod of Asclepius, Bragi''s
    Harp, Heartseeker, Erosion, Pharaoh''s Curse, Tekko-Kagi, Stone of Binding, Eye
    of Providence, Tyrfing, Shield of the Phoenix, Draconic Scale, Shogun''s Ofuda,
    Jade Scepter, Doom Orb, Wish-Granting Pearl, Avenging Blade, Death Metal, Chronos''
    Pendant, Magi''s Cloak.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.35
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.68
      pick: 0.18
      fit: 0.36
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.27
      fit: 0.33
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.53
      win: 0.85
      pick: 0.15
      fit: 0.29
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Shifter's Shield
  - Freya's Tears
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s
    Revenge, Kinetic Cuirass, Shield Splitter, Genji''s Guard, Breastplate of Valor,
    Golden Blade, Runeforged Hammer, Eye of the Storm, Erosion, Pharaoh''s Curse,
    Eye of Providence, Lernaean Bow, Draconic Scale, Shogun''s Ofuda, Hydra''s Lament,
    Shield of the Phoenix, Stone of Binding, Tyrfing, Nimble Ring, Helm of Radiance,
    Gluttonous Grimoire, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Screeching
    Gargoyle, Midgardian Mail, Bragi''s Harp, Tekko-Kagi, Daybreak Gavel, Spear of
    Desolation, Heartseeker, Rod of Asclepius, Leviathan''s Hide, Void Shield, Stampede,
    Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.64
      pick: 0.12
      fit: 0.58
    Shield Splitter:
      total: 0.56
      efficiency: 0.55
      win: 0.64
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.27
      fit: 0.43
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---

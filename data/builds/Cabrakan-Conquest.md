---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.0
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.3
    win_rate: 0.44
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.22
      win_rate: 0.58
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.43
  - name: Genji's Guard
    pick_rate: 0.22
    win_rate: 0.58
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.19
      win_rate: 0.7
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.29
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.75
    alternates:
    - name: Genji's Guard
      pick_rate: 0.31
      win_rate: 0.44
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.25
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.6
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.4
  - name: Medal of Defense
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.33
    - name: Engraved Guard
      pick_rate: 0.08
      win_rate: 0.0
  - name: Sage's Ring
    pick_rate: 0.13
    win_rate: 0.33
    alternates:
    - name: Captain's Ring
      pick_rate: 0.08
      win_rate: 0.5
    - name: Shield
      pick_rate: 0.08
      win_rate: 0.5
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.43
    win_rate: 0.3
  - name: Bumba's Hammer
    pick_rate: 0.2
    win_rate: 0.82
  - name: Heroism
    pick_rate: 0.07
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-09-11'
  god_win_rate: 0.42592592592592593
  god_matches_won: 23
  god_matches_played: 54
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-11'
  god_matches_analyzed: 3080
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Kinetic Cuirass, Shield
    Splitter, Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence, Draconic
    Scale, Shield of the Phoenix, Stone of Binding, Hydra''s Lament, Magi''s Cloak,
    Helm of Radiance, Gluttonous Grimoire, Avenging Blade, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Leviathan''s Hide, Void Shield, Ancile, Heartseeker,
    Oni Hunter''s Garb, Spear of Desolation, Prophetic Cloak, Daybreak Gavel, Rod
    of Asclepius, Void Stone, Xibalban Effigy, Spectral Armor, Helm of Darkness, Soul
    Gem, Spear of the Magus, Stampede, Hide of the Nemean Lion.'
  slot_scores:
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.7
      pick: 0.26
      fit: 0.31
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.58
      pick: 0.3
      fit: 0.31
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.37
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.22
      fit: 0.48
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.2
      fit: 0.52
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Runeforged Hammer
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield of the Phoenix
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield of the Phoenix,
    Kinetic Cuirass, Rod of Asclepius, Shield Splitter, Soul Gem, Eye of the Storm,
    Berserker''s Shield, Erosion, Ethereal Staff, Eye of Providence, The Reaper, Draconic
    Scale, Yogi''s Necklace, Hydra''s Lament, Phoenix Feather, Gluttonous Grimoire,
    Avenging Blade, Chandra''s Grace, Glorious Pridwen, Lifebinder, Stone of Binding,
    Midgardian Mail, Helm of Radiance, Daybreak Gavel, Magi''s Cloak, Leviathan''s
    Hide, Void Shield, Sphere of Negation, Ancile, Screeching Gargoyle, Heartseeker,
    Oni Hunter''s Garb, Stampede, Hide of the Nemean Lion.'
  slot_scores:
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.7
      pick: 0.26
      fit: 0.28
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.58
      pick: 0.3
      fit: 0.28
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.39
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.8
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.22
      fit: 0.54
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Stone of Binding
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
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Kinetic Cuirass, Gluttonous Grimoire, Avenging Blade, Screeching Gargoyle, Void
    Shield, Spear of Desolation, Heartseeker, Spear of the Magus, Shield Splitter,
    Void Stone, Soul Gem, Obsidian Shard, Berserker''s Shield, Titan''s Bane, The
    Crusher, Eye of the Storm, Erosion, The Reaper, Hydra''s Lament, Eye of Providence,
    Shield of the Phoenix, Draconic Scale, Helm of Radiance, Doom Orb, The World Stone,
    Magi''s Cloak, Pendulum Blade, Dreamer''s Idol, Avatar''s Parashu, Mantle Of Discord,
    Midgardian Mail, Daybreak Gavel, Rod of Asclepius.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.7
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.7
      pick: 0.26
      fit: 0.23
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.3
      fit: 0.23
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.54
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.22
      fit: 0.38
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Runeforged Hammer
  - Nimble Ring
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Tyrfing, Shield
    Splitter, Pharaoh''s Curse, Soul Gem, Riptalon, Lernaean Bow, Shogun''s Ofuda,
    Silverbranch Bow, Erosion, Helm of Radiance, Eye of Providence, Stone of Binding,
    Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Toxic Blade, Draconic
    Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Midgardian
    Mail, Mantle Of Discord, Spear of Desolation, Bragi''s Harp, Spear of the Magus,
    Tekko-Kagi, Rod of Asclepius, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.3
      fit: 0.2
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.7
      pick: 0.26
      fit: 0.2
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.58
      pick: 0.22
      fit: 0.31
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.3
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Hydra''s
    Lament, Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Shield Splitter, Berserker''s
    Shield, Prophetic Cloak, Erosion, Helm of Radiance, Gluttonous Grimoire, Eye of
    Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding, Eye of the
    Storm, Arondight, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus,
    Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak
    Gavel, Chandra''s Grace, Obsidian Shard, Leviathan''s Hide, Jade Scepter, Void
    Shield, Hide of the Nemean Lion.'
  slot_scores:
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.7
      pick: 0.26
      fit: 0.48
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.58
      pick: 0.3
      fit: 0.48
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.46
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.58
      pick: 0.22
      fit: 0.32
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.2
      fit: 0.64
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Runeforged Hammer
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Runeforged Hammer
  - Transcendence
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Golden Blade, Eye of
    the Storm, Gluttonous Grimoire, Hydra''s Lament, Heartseeker, Lernaean Bow, Erosion,
    Spear of Desolation, Tekko-Kagi, Eye of Providence, Tyrfing, Avenging Blade, Spear
    of the Magus, Shield of the Phoenix, Stone of Binding, Draconic Scale, Helm of
    Radiance, Titan''s Bane, Soul Gem, The Crusher, Obsidian Shard, Pharaoh''s Curse,
    Magi''s Cloak, The Reaper, Silverbranch Bow, Nimble Ring, Shogun''s Ofuda, Screeching
    Gargoyle, Mantle Of Discord, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.41
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.04
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.7
      pick: 0.26
      fit: 0.23
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.3
      fit: 0.23
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.22
      fit: 0.44
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.22
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Runeforged Hammer
  - Transcendence
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter, Spear of
    Desolation, Spear of the Magus, Helm of Radiance, Soul Gem, Obsidian Shard, Berserker''s
    Shield, Eye of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker, Erosion,
    Eye of Providence, Shield of the Phoenix, Stone of Binding, Draconic Scale, Doom
    Orb, Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging Blade, Magi''s Cloak,
    Chronos'' Pendant, The World Stone, Helm of Darkness, Titan''s Bane, The Crusher,
    Ancient Signet, Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian
    Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.18
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.7
      pick: 0.26
      fit: 0.23
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.58
      pick: 0.3
      fit: 0.23
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.41
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.22
      fit: 0.4
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.18
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Shifter's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Kinetic
    Cuirass, Shield Splitter, Eye of the Storm, Berserker''s Shield, Erosion, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding, Hydra''s
    Lament, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Avenging Blade,
    Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Hide of the Nemean Lion,
    Leviathan''s Hide, Void Shield, Stampede, Ancile, Heartseeker, Oni Hunter''s Garb,
    Spear of Desolation, Prophetic Cloak, Daybreak Gavel, Rod of Asclepius, Void Stone,
    Xibalban Effigy, Spectral Armor, Helm of Darkness, Soul Gem, Spear of the Magus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.67
    Shield Splitter:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.49
      efficiency: 0.55
      win: 0.44
      pick: 0.3
      fit: 0.57
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.2
      fit: 0.52
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
---

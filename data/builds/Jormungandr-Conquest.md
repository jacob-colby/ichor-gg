---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.24
  aspect_win_rate: 0.67
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.41
    win_rate: 0.6
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.57
    - name: Leviathan's Hide
      pick_rate: 0.16
      win_rate: 0.67
  - name: Sanguine Lash
    pick_rate: 0.19
    win_rate: 0.43
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.19
      win_rate: 0.71
    - name: Sun Beam Bow
      pick_rate: 0.08
      win_rate: 1.0
  - name: Golden Blade
    pick_rate: 0.14
    win_rate: 0.6
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.2
    - name: Ethereal Staff
      pick_rate: 0.11
      win_rate: 0.5
  - name: Kinetic Cuirass
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.16
      win_rate: 0.33
    - name: Hide of the Nemean Lion
      pick_rate: 0.11
      win_rate: 0.75
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.0
    - name: Brawler’s Beat Stick
      pick_rate: 0.08
      win_rate: 0.67
  - name: Medallion
    pick_rate: 0.07
    win_rate: 1.0
    alternates:
    - name: Soul Reaver
      pick_rate: 0.07
      win_rate: 0.5
    - name: Stalwart Sigil
      pick_rate: 0.07
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.35
    win_rate: 0.38
  - name: Sundering Axe
    pick_rate: 0.19
    win_rate: 0.57
  - name: Bluestone Pendant
    pick_rate: 0.14
    win_rate: 0.8
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-10-08'
  god_win_rate: 0.5675675675675675
  god_matches_won: 21
  god_matches_played: 37
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-08'
  god_matches_analyzed: 1596
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Sun Beam Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Prophetic Cloak
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Prophetic Cloak
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Shield Splitter, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Eye
    of the Storm, Erosion, Pharaoh''s Curse, Eye of Providence, Lernaean Bow, Draconic
    Scale, Shogun''s Ofuda, Hydra''s Lament, Shield of the Phoenix, Stone of Binding,
    Tyrfing, Nimble Ring, Helm of Radiance, Gluttonous Grimoire, Magi''s Cloak, Avenging
    Blade, Mantle Of Discord, Screeching Gargoyle, Midgardian Mail, Bragi''s Harp,
    Tekko-Kagi, Daybreak Gavel, Spear of Desolation, Heartseeker, Rod of Asclepius,
    Void Shield, Stampede, Ancile.'
  slot_scores:
    Sun Beam Bow:
      total: 0.63
      efficiency: 0.41
      win: 1.0
      pick: 0.11
      fit: 0.21
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.31
    Prophetic Cloak:
      total: 0.55
      efficiency: 0.44
      win: 0.71
      pick: 0.26
      fit: 0.43
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.52
      win: 0.75
      pick: 0.18
      fit: 0.31
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Sun Beam Bow
  - Prophetic Cloak
  - Hide of the Nemean Lion
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Sun Beam Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Leviathan's Hide — physical protection
    swap_item: Leviathan's Hide
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge,
    Shield of the Phoenix, Rod of Asclepius, Soul Gem, Runeforged Hammer, Genji''s
    Guard, Breastplate of Valor, Shield Splitter, Eye of the Storm, Pharaoh''s Curse,
    The Reaper, Yogi''s Necklace, Lernaean Bow, Erosion, Shogun''s Ofuda, Hydra''s
    Lament, Gluttonous Grimoire, Eye of Providence, Phoenix Feather, Tyrfing, Chandra''s
    Grace, Riptalon, Draconic Scale, Nimble Ring, Avenging Blade, Lifebinder, Helm
    of Radiance, Stone of Binding, Glorious Pridwen, Daybreak Gavel, Midgardian Mail,
    Bragi''s Harp, Tekko-Kagi, Sphere of Negation.'
  slot_scores:
    Sun Beam Bow:
      total: 0.63
      efficiency: 0.41
      win: 1.0
      pick: 0.11
      fit: 0.22
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.49
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.32
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.71
    Hide of the Nemean Lion:
      total: 0.58
      efficiency: 0.52
      win: 0.75
      pick: 0.18
      fit: 0.32
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.76
  community_ordered:
  - Sun Beam Bow
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Sun Beam Bow
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Prophetic Cloak — physical protection
    swap_item: Prophetic Cloak
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield, Amanita Charm,
    Stone of Binding, Avenging Blade, Screeching Gargoyle, Gluttonous Grimoire, Genji''s
    Guard, Void Shield, Breastplate of Valor, Spear of Desolation, Spear of the Magus,
    Void Stone, Heartseeker, Shield Splitter, Soul Gem, Tekko-Kagi, Obsidian Shard,
    Runeforged Hammer, Silverbranch Bow, Toxic Blade, Titan''s Bane, The Crusher,
    Eye of the Storm, Hydra''s Lament, Lernaean Bow, Erosion, Nimble Ring, Pharaoh''s
    Curse, The Reaper, Helm of Radiance, Eye of Providence, Shield of the Phoenix,
    Draconic Scale, Doom Orb, Shogun''s Ofuda, Tyrfing.'
  slot_scores:
    Sun Beam Bow:
      total: 0.62
      efficiency: 0.41
      win: 1.0
      pick: 0.11
      fit: 0.16
    Stone of Binding:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.66
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.47
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.52
      win: 0.75
      pick: 0.18
      fit: 0.24
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Sun Beam Bow
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Sun Beam Bow
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Gluttonous Grimoire, Genji''s Guard, Breastplate of Valor, Tyrfing,
    Shield Splitter, Runeforged Hammer, Soul Gem, Pharaoh''s Curse, Riptalon, Lernaean
    Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance, Eye of Providence,
    Stone of Binding, Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Toxic
    Blade, Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The
    Reaper, Spear of Desolation, Spear of the Magus, Bragi''s Harp, Midgardian Mail,
    Mantle Of Discord, Tekko-Kagi, Rod of Asclepius, Avenging Blade.'
  slot_scores:
    Sun Beam Bow:
      total: 0.65
      efficiency: 0.41
      win: 1.0
      pick: 0.11
      fit: 0.33
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.22
      fit: 0.54
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.21
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.52
      win: 0.75
      pick: 0.18
      fit: 0.24
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Sun Beam Bow
  - Golden Blade
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Sun Beam Bow
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Prophetic Cloak
  - Hide of the Nemean Lion
  flex_slots:
  - Hide of the Nemean Lion
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Genji''s Guard, Breastplate of Valor, Amanita Charm, Shield
    of the Phoenix, Spear of Desolation, Hydra''s Lament, Screeching Gargoyle, Soul
    Gem, Chronos'' Pendant, Shield Splitter, Nimble Ring, Runeforged Hammer, Helm
    of Radiance, Gluttonous Grimoire, Erosion, Pharaoh''s Curse, Eye of Providence,
    Stone of Binding, Draconic Scale, Shogun''s Ofuda, Gladiator''s Shield, Eye of
    the Storm, Arondight, Gem of Focus, Lernaean Bow, Spear of the Magus, Magi''s
    Cloak, Rod of Asclepius, Daybreak Gavel, Mantle Of Discord, Obsidian Shard, Midgardian
    Mail, Eye of Erebus, Tyrfing.'
  slot_scores:
    Sun Beam Bow:
      total: 0.62
      efficiency: 0.41
      win: 1.0
      pick: 0.11
      fit: 0.17
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.41
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.39
    Prophetic Cloak:
      total: 0.57
      efficiency: 0.44
      win: 0.71
      pick: 0.26
      fit: 0.55
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.52
      win: 0.75
      pick: 0.18
      fit: 0.25
  community_ordered:
  - Sun Beam Bow
  - Prophetic Cloak
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Sun Beam Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Prophetic Cloak
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Prophetic Cloak
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Shield Splitter, Runeforged Hammer, Genji''s Guard, Breastplate
    of Valor, Eye of the Storm, Gluttonous Grimoire, Hydra''s Lament, Heartseeker,
    Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi, Eye of Providence, Spear
    of the Magus, Avenging Blade, Shield of the Phoenix, Stone of Binding, Draconic
    Scale, Helm of Radiance, Tyrfing, Titan''s Bane, Soul Gem, The Crusher, Obsidian
    Shard, Pharaoh''s Curse, Magi''s Cloak, The Reaper, Nimble Ring, Shogun''s Ofuda,
    Screeching Gargoyle, Mantle Of Discord, Midgardian Mail, Daybreak Gavel, Silverbranch
    Bow.'
  slot_scores:
    Sun Beam Bow:
      total: 0.62
      efficiency: 0.41
      win: 1.0
      pick: 0.11
      fit: 0.12
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.45
    Prophetic Cloak:
      total: 0.54
      efficiency: 0.44
      win: 0.71
      pick: 0.26
      fit: 0.38
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.52
      win: 0.75
      pick: 0.18
      fit: 0.27
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Sun Beam Bow
  - Prophetic Cloak
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Sun Beam Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Prophetic Cloak
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Prophetic Cloak
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Gluttonous Grimoire, Genji''s Guard, Breastplate
    of Valor, Shield Splitter, Spear of the Magus, Spear of Desolation, Nimble Ring,
    Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian Shard, Eye of the Storm,
    Hydra''s Lament, Lernaean Bow, Rod of Asclepius, Bragi''s Harp, Heartseeker, Erosion,
    Pharaoh''s Curse, Tekko-Kagi, Stone of Binding, Eye of Providence, Tyrfing, Shield
    of the Phoenix, Draconic Scale, Shogun''s Ofuda, Jade Scepter, Doom Orb, Silverbranch
    Bow, Wish-Granting Pearl, Avenging Blade, Death Metal, Chronos'' Pendant, Magi''s
    Cloak.'
  slot_scores:
    Sun Beam Bow:
      total: 0.62
      efficiency: 0.41
      win: 1.0
      pick: 0.11
      fit: 0.16
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.35
    Prophetic Cloak:
      total: 0.54
      efficiency: 0.44
      win: 0.71
      pick: 0.26
      fit: 0.33
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.52
      win: 0.75
      pick: 0.18
      fit: 0.23
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Sun Beam Bow
  - Prophetic Cloak
  - Hide of the Nemean Lion
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
    Revenge, Shield Splitter, Genji''s Guard, Breastplate of Valor, Runeforged Hammer,
    Eye of the Storm, Erosion, Pharaoh''s Curse, Eye of Providence, Lernaean Bow,
    Draconic Scale, Shogun''s Ofuda, Hydra''s Lament, Shield of the Phoenix, Stone
    of Binding, Tyrfing, Nimble Ring, Helm of Radiance, Gluttonous Grimoire, Magi''s
    Cloak, Avenging Blade, Mantle Of Discord, Screeching Gargoyle, Midgardian Mail,
    Bragi''s Harp, Tekko-Kagi, Daybreak Gavel, Spear of Desolation, Heartseeker, Rod
    of Asclepius, Void Shield, Stampede, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.27
      fit: 0.58
    Shield Splitter:
      total: 0.54
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.35
      fit: 0.43
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---

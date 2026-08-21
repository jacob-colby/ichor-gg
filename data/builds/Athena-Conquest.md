---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.32
  aspect_win_rate: 0.53
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.16
    win_rate: 0.52
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.14
      win_rate: 0.53
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.59
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.56
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.55
  - name: Breastplate of Valor
    pick_rate: 0.08
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.6
    - name: Hydra's Lament
      pick_rate: 0.07
      win_rate: 0.59
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.71
    alternates:
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.49
    - name: Deathbringer
      pick_rate: 0.06
      win_rate: 0.5
  - name: Hide of the Nemean Lion
    pick_rate: 0.05
    win_rate: 0.51
    alternates:
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.66
    - name: Deathbringer
      pick_rate: 0.05
      win_rate: 0.61
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.6
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.05
      win_rate: 0.64
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.41
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.21
    win_rate: 0.58
  - name: Bumba's Cudgel
    pick_rate: 0.19
    win_rate: 0.52
  - name: Selflessness
    pick_rate: 0.18
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-08-21'
  god_win_rate: 0.5494367959949937
  god_matches_won: 439
  god_matches_played: 799
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Berserker''s
    Shield, Jotunn''s Revenge, Shield of the Phoenix, Mantle Of Discord, Stone of
    Binding, Erosion, Gluttonous Grimoire, Eye of Providence, Breastplate of Valor,
    Draconic Scale, Shield Splitter, Spectral Armor, Leviathan''s Hide, Magi''s Cloak,
    Pharaoh''s Curse, Helm of Radiance, Soul Gem, Runeforged Hammer, Eye of the Storm,
    Shogun''s Ofuda, Stampede, Midgardian Mail, Screeching Gargoyle, Golden Blade,
    Doublet of Binding, Nimble Ring, Void Shield, Ancile, Ethereal Staff, Spear of
    Desolation, Oni Hunter''s Garb, Prophetic Cloak, Rod of Asclepius, Daybreak Gavel,
    Death Metal, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.19
      fit: 0.32
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.21
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.68
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.71
      pick: 0.12
      fit: 0.53
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.58
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Shield of the Phoenix, Rod of Tahuti,
    Kinetic Cuirass, Berserker''s Shield, Soul Gem, Ethereal Staff, Rod of Asclepius,
    Jotunn''s Revenge, Gluttonous Grimoire, Phoenix Feather, Chandra''s Grace, Erosion,
    Eye of Providence, Breastplate of Valor, Draconic Scale, Spectral Armor, Yogi''s
    Necklace, Mantle Of Discord, Stone of Binding, Riptalon, Runeforged Hammer, The
    Reaper, Shield Splitter, Leviathan''s Hide, Pharaoh''s Curse, Lifebinder, Eye
    of the Storm, Glorious Pridwen, Golden Blade, Shogun''s Ofuda, Midgardian Mail,
    Helm of Radiance, Blood-Bound Book, Daybreak Gavel, Spirit Robe, Doublet of Binding,
    Magi''s Cloak, Hide of the Nemean Lion.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.22
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.71
      pick: 0.12
      fit: 0.46
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Gluttonous Grimoire
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Freya''s Tears, Jotunn''s Revenge, Stone of Binding,
    Gluttonous Grimoire, Amanita Charm, Kinetic Cuirass, Berserker''s Shield, Soul
    Gem, Screeching Gargoyle, The Crusher, Void Shield, Spear of Desolation, Spear
    of the Magus, Void Stone, Obsidian Shard, Avenging Blade, Shield of the Phoenix,
    Breastplate of Valor, Mantle Of Discord, Silverbranch Bow, Heartseeker, Erosion,
    Shield Splitter, The Reaper, Spectral Armor, Toxic Blade, Eye of Providence, Riptalon,
    Draconic Scale, Helm of Radiance, Doom Orb, Runeforged Hammer, The Cosmic Horror,
    Leviathan''s Hide, Nimble Ring, Pharaoh''s Curse, The World Stone, Magi''s Cloak,
    Titan''s Bane.'
  slot_scores:
    Stone of Binding:
      total: 0.56
      efficiency: 0.54
      win: 0.59
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.53
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.71
      pick: 0.12
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.59
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s
    Revenge, Kinetic Cuirass, Nimble Ring, Golden Blade, Gluttonous Grimoire, Pharaoh''s
    Curse, Shogun''s Ofuda, Tyrfing, Shield Splitter, Breastplate of Valor, Shield
    of the Phoenix, Mantle Of Discord, Soul Gem, Runeforged Hammer, Stone of Binding,
    Riptalon, Lernaean Bow, Silverbranch Bow, Hydra''s Lament, Spectral Armor, Death
    Metal, The Crusher, Erosion, Helm of Radiance, Eye of Providence, Eye of the Storm,
    Toxic Blade, Draconic Scale, Leviathan''s Hide, Magi''s Cloak, Screeching Gargoyle,
    Daybreak Gavel, The Reaper, Spear of Desolation, Spear of the Magus, Bragi''s
    Harp.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.2
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.71
      pick: 0.12
      fit: 0.33
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Jotunn''s
    Revenge, Amanita Charm, Kinetic Cuirass, Breastplate of Valor, Shield of the Phoenix,
    Berserker''s Shield, Soul Gem, Hydra''s Lament, Spear of Desolation, Gluttonous
    Grimoire, Screeching Gargoyle, Mantle Of Discord, Chronos'' Pendant, Shield Splitter,
    Stone of Binding, Runeforged Hammer, Helm of Radiance, Prophetic Cloak, Nimble
    Ring, Erosion, Death Metal, Spectral Armor, Eye of Providence, Draconic Scale,
    Gladiator''s Shield, The Crusher, Chandra''s Grace, Eye of the Storm, Leviathan''s
    Hide, Arondight, Pharaoh''s Curse, Gem of Focus, Ethereal Staff, Magi''s Cloak,
    Spear of the Magus, Rod of Asclepius, Golden Blade, Eye of Erebus.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.19
      fit: 0.43
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.12
      fit: 0.43
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.5
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.71
      pick: 0.12
      fit: 0.58
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, The
    Crusher, Shield Splitter, Runeforged Hammer, Golden Blade, Hydra''s Lament, Soul
    Gem, Death Metal, Breastplate of Valor, Eye of the Storm, Shield of the Phoenix,
    Mantle Of Discord, Nimble Ring, Stone of Binding, Heartseeker, The Reaper, Pharaoh''s
    Curse, Tyrfing, Lernaean Bow, Spear of Desolation, Spear of the Magus, Spectral
    Armor, Erosion, Shogun''s Ofuda, Helm of Radiance, Avenging Blade, Eye of Providence,
    Tekko-Kagi, Obsidian Shard, Draconic Scale, Titan''s Bane, Silverbranch Bow, Leviathan''s
    Hide, Magi''s Cloak.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.71
      pick: 0.12
      fit: 0.34
    The Crusher:
      total: 0.53
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Death Metal
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Freya''s Tears, Jotunn''s
    Revenge, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Berserker''s Shield,
    Soul Gem, Death Metal, The Crusher, Shield Splitter, Spear of Desolation, Spear
    of the Magus, Runeforged Hammer, Helm of Radiance, Nimble Ring, Obsidian Shard,
    Breastplate of Valor, Shield of the Phoenix, Hydra''s Lament, Mantle Of Discord,
    Stone of Binding, Eye of the Storm, Ethereal Staff, Rod of Asclepius, Heartseeker,
    Spectral Armor, Golden Blade, The Reaper, Erosion, Eye of Providence, Draconic
    Scale, Leviathan''s Hide, Jade Scepter, Doom Orb, Pharaoh''s Curse, The Cosmic
    Horror, Wish-Granting Pearl, Avenging Blade, Chronos'' Pendant.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.48
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.32
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.71
      pick: 0.12
      fit: 0.34
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Berserker''s
    Shield, Freya''s Tears, Jotunn''s Revenge, Breastplate of Valor, Shield of the
    Phoenix, Mantle Of Discord, Stone of Binding, Erosion, Gluttonous Grimoire, Eye
    of Providence, Draconic Scale, Shield Splitter, Spectral Armor, Leviathan''s Hide,
    Magi''s Cloak, Pharaoh''s Curse, Helm of Radiance, Soul Gem, Runeforged Hammer,
    Eye of the Storm, Shogun''s Ofuda, Midgardian Mail, Screeching Gargoyle, Hide
    of the Nemean Lion, Golden Blade, Doublet of Binding, Nimble Ring, Void Shield,
    Stampede, Ancile, Ethereal Staff, Spear of Desolation, Oni Hunter''s Garb, Prophetic
    Cloak, Rod of Asclepius, Daybreak Gavel, Death Metal.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.21
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.68
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.71
      pick: 0.12
      fit: 0.53
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.52
      pick: 0.16
      fit: 0.58
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.58
  starter: *id001
---

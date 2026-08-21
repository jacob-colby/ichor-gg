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
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Jotunn's Revenge
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Berserker''s
    Shield, Jotunn''s Revenge, Shield of the Phoenix, Erosion, Eye of Providence,
    Mantle Of Discord, Stone of Binding, Draconic Scale, Shield Splitter, Gluttonous
    Grimoire, Breastplate of Valor, Spectral Armor, Magi''s Cloak, Leviathan''s Hide,
    Pharaoh''s Curse, Eye of the Storm, Helm of Radiance, Soul Gem, Shogun''s Ofuda,
    Stampede, Midgardian Mail, Runeforged Hammer, Screeching Gargoyle, Prophetic Cloak,
    Doublet of Binding, Void Shield, Ancile, Oni Hunter''s Garb, Helm of Darkness,
    Xibalban Effigy, Void Stone, Ethereal Staff, Spear of Desolation, Hussar''s Wings,
    Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.71
      pick: 0.12
      fit: 0.62
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.68
    Erosion:
      total: 0.55
      efficiency: 0.51
      win: 0.59
      pick: 0.0
      fit: 0.68
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
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Shield of the Phoenix, Kinetic Cuirass,
    Rod of Tahuti, Berserker''s Shield, Soul Gem, Ethereal Staff, Rod of Asclepius,
    Jotunn''s Revenge, Gluttonous Grimoire, Erosion, Phoenix Feather, Eye of Providence,
    Chandra''s Grace, Draconic Scale, Spectral Armor, Breastplate of Valor, Mantle
    Of Discord, Stone of Binding, Yogi''s Necklace, Shield Splitter, Leviathan''s
    Hide, Pharaoh''s Curse, Runeforged Hammer, Glorious Pridwen, Eye of the Storm,
    The Reaper, Shogun''s Ofuda, Lifebinder, Stampede, Midgardian Mail, Helm of Radiance,
    Doublet of Binding, Spirit Robe, Void Shield, Magi''s Cloak, Ancile, Oni Hunter''s
    Garb, Hide of the Nemean Lion.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.46
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.71
      pick: 0.12
      fit: 0.54
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.96
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
  - Stone of Binding
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
    for this god: Rod of Tahuti, Freya''s Tears, Jotunn''s Revenge, Gluttonous Grimoire,
    Stone of Binding, Amanita Charm, Kinetic Cuirass, Soul Gem, Berserker''s Shield,
    Screeching Gargoyle, Spear of Desolation, The Crusher, Void Shield, Spear of the
    Magus, Void Stone, Obsidian Shard, Avenging Blade, Shield of the Phoenix, Mantle
    Of Discord, Breastplate of Valor, Heartseeker, Erosion, Shield Splitter, The Reaper,
    Eye of Providence, Spectral Armor, Draconic Scale, Doom Orb, The Cosmic Horror,
    Helm of Radiance, Runeforged Hammer, The World Stone, Leviathan''s Hide, Pharaoh''s
    Curse, Titan''s Bane, Magi''s Cloak, Dreamer''s Idol, Silverbranch Bow, Nimble
    Ring, Toxic Blade.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.54
      win: 0.59
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.71
      pick: 0.12
      fit: 0.43
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.59
      pick: 0.0
      fit: 0.39
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
    Revenge, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Breastplate of
    Valor, Soul Gem, Berserker''s Shield, Hydra''s Lament, Spear of Desolation, Screeching
    Gargoyle, Gluttonous Grimoire, Chronos'' Pendant, Shield Splitter, Mantle Of Discord,
    Stone of Binding, Prophetic Cloak, Erosion, Helm of Radiance, Runeforged Hammer,
    Eye of Providence, Gladiator''s Shield, Spectral Armor, Death Metal, Draconic
    Scale, Nimble Ring, Chandra''s Grace, Eye of the Storm, Arondight, Gem of Focus,
    Leviathan''s Hide, Pharaoh''s Curse, The Crusher, Magi''s Cloak, Ethereal Staff,
    Rod of Asclepius, Eye of Erebus, Spear of the Magus, Totem of Death.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.19
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.12
      fit: 0.48
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.71
      pick: 0.12
      fit: 0.64
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.45
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, The
    Crusher, Shield Splitter, Runeforged Hammer, Hydra''s Lament, Soul Gem, Eye of
    the Storm, Death Metal, Shield of the Phoenix, Breastplate of Valor, Mantle Of
    Discord, Stone of Binding, Heartseeker, The Reaper, Nimble Ring, Golden Blade,
    Pharaoh''s Curse, Lernaean Bow, Erosion, Spear of Desolation, Spectral Armor,
    Tekko-Kagi, Spear of the Magus, Eye of Providence, Shogun''s Ofuda, Avenging Blade,
    Draconic Scale, Helm of Radiance, Titan''s Bane, Obsidian Shard, Leviathan''s
    Hide, Magi''s Cloak, Tyrfing, Screeching Gargoyle.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.71
      pick: 0.12
      fit: 0.38
    The Crusher:
      total: 0.54
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.42
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
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Freya''s Tears, Jotunn''s
    Revenge, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Berserker''s Shield,
    Soul Gem, Death Metal, The Crusher, Shield Splitter, Spear of Desolation, Spear
    of the Magus, Runeforged Hammer, Helm of Radiance, Obsidian Shard, Nimble Ring,
    Shield of the Phoenix, Breastplate of Valor, Mantle Of Discord, Stone of Binding,
    Hydra''s Lament, Eye of the Storm, Ethereal Staff, Rod of Asclepius, Heartseeker,
    Erosion, Spectral Armor, The Reaper, Eye of Providence, Draconic Scale, Doom Orb,
    Jade Scepter, The Cosmic Horror, Leviathan''s Hide, Pharaoh''s Curse, Wish-Granting
    Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.27
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
      fit: 0.52
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.59
      pick: 0.0
      fit: 0.36
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.71
      pick: 0.12
      fit: 0.38
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.42
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
  - Shifter's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Freya''s
    Tears, Berserker''s Shield, Jotunn''s Revenge, Shield of the Phoenix, Breastplate
    of Valor, Erosion, Eye of Providence, Mantle Of Discord, Stone of Binding, Draconic
    Scale, Shield Splitter, Gluttonous Grimoire, Spectral Armor, Magi''s Cloak, Leviathan''s
    Hide, Pharaoh''s Curse, Eye of the Storm, Helm of Radiance, Soul Gem, Shogun''s
    Ofuda, Midgardian Mail, Runeforged Hammer, Screeching Gargoyle, Hide of the Nemean
    Lion, Prophetic Cloak, Doublet of Binding, Void Shield, Stampede, Ancile, Oni
    Hunter''s Garb, Helm of Darkness, Xibalban Effigy, Void Stone, Ethereal Staff,
    Spear of Desolation, Hussar''s Wings, Rod of Asclepius.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.71
      pick: 0.12
      fit: 0.62
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.52
      pick: 0.16
      fit: 0.68
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.68
  starter: *id001
---

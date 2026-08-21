---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.6
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.41
    win_rate: 0.58
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.26
      win_rate: 0.39
    - name: Avenging Blade
      pick_rate: 0.08
      win_rate: 0.53
  - name: Hydra's Lament
    pick_rate: 0.29
    win_rate: 0.53
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.43
    - name: Transcendence
      pick_rate: 0.09
      win_rate: 0.58
  - name: Shifter's Shield
    pick_rate: 0.14
    win_rate: 0.51
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.12
      win_rate: 0.63
    - name: The Reaper
      pick_rate: 0.09
      win_rate: 0.55
  - name: Heartseeker
    pick_rate: 0.18
    win_rate: 0.54
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.48
    - name: The Reaper
      pick_rate: 0.06
      win_rate: 0.59
  - name: Titan's Bane
    pick_rate: 0.12
    win_rate: 0.51
    alternates:
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.56
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.7
  - name: Blinking Abyss
    pick_rate: 0.08
    win_rate: 0.6
    alternates:
    - name: Skeggox
      pick_rate: 0.07
      win_rate: 0.77
    - name: Titan's Bane
      pick_rate: 0.06
      win_rate: 0.73
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.27
    win_rate: 0.6
  - name: Bumba's Cudgel
    pick_rate: 0.25
    win_rate: 0.48
  - name: Hunter's Cowl
    pick_rate: 0.16
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-08-21'
  god_win_rate: 0.531578947368421
  god_matches_won: 202
  god_matches_played: 380
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Death Metal
  - The Crusher
  flex_slots:
  - Tyrfing
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Death Metal, The Crusher, Berserker''s Shield, Nimble
    Ring, Tyrfing, Golden Blade, Tekko-Kagi, Lernaean Bow, Silverbranch Bow, The Reaper,
    Gluttonous Grimoire, Riptalon, Soul Gem, Spear of the Magus, Runeforged Hammer,
    Bragi''s Harp, Spear of Desolation, Obsidian Shard, Toxic Blade, Dominance, Genji''s
    Guard, Deathbringer, Damaru, Breastplate of Valor, Amanita Charm, Kinetic Cuirass,
    Pharaoh''s Curse, Demon Blade, Shield Splitter, Bracer of The Abyss, Musashi''s
    Dual Swords, Freya''s Tears, Doom Orb, The Cosmic Horror, Shogun''s Ofuda, Avenging
    Blade, Avatar''s Parashu.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.22
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.58
      pick: 0.41
      fit: 0.43
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.58
      pick: 0.12
      fit: 0.22
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.55
      pick: 0.0
      fit: 0.65
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.45
    The Crusher:
      total: 0.52
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.49
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Death Metal
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of Desolation,
    The Crusher, Spear of the Magus, Berserker''s Shield, Genji''s Guard, Obsidian
    Shard, Breastplate of Valor, Bragi''s Harp, The Reaper, Lernaean Bow, Transcendence,
    Tyrfing, Doom Orb, Golden Blade, Runeforged Hammer, Ancient Signet, Tekko-Kagi,
    The World Stone, Helm of Radiance, Chronos'' Pendant, Silverbranch Bow, The Cosmic
    Horror, Bracer of The Abyss, Dominance, Freya''s Tears, Amanita Charm, Ethereal
    Staff, Riptalon, Rod of Asclepius, Wish-Granting Pearl, Kinetic Cuirass, Dreamer''s
    Idol, Deathbringer.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.58
      pick: 0.41
      fit: 0.48
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.58
      pick: 0.12
      fit: 0.26
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.53
      pick: 0.4
      fit: 0.46
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.55
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Death Metal
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Shield of the Phoenix,
    Soul Gem, The Reaper, Kinetic Cuirass, Riptalon, Ethereal Staff, Rod of Asclepius,
    Gluttonous Grimoire, Death Metal, Golden Blade, Runeforged Hammer, Nimble Ring,
    The Crusher, Freya''s Tears, Pharaoh''s Curse, Genji''s Guard, Breastplate of
    Valor, Phoenix Feather, Yogi''s Necklace, Shield Splitter, Shogun''s Ofuda, Chandra''s
    Grace, Eye of the Storm, Mantle Of Discord, Spectral Armor, Stone of Binding,
    Blood-Bound Book, Lernaean Bow, Tyrfing, Erosion, Spear of the Magus, Silverbranch
    Bow, Eye of Providence, Lifebinder, Toxic Blade, Leviathan''s Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.58
      pick: 0.41
      fit: 0.27
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.46
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.58
    Death Metal:
      total: 0.5
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.28
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Silverbranch Bow
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  flex_slots:
  - Silverbranch Bow
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, The Crusher, Gluttonous Grimoire, The Reaper, Soul
    Gem, Silverbranch Bow, Tekko-Kagi, Riptalon, Spear of the Magus, Death Metal,
    Obsidian Shard, Spear of Desolation, Berserker''s Shield, Nimble Ring, Avenging
    Blade, Toxic Blade, Tyrfing, Stone of Binding, Golden Blade, Lernaean Bow, Doom
    Orb, The Cosmic Horror, Screeching Gargoyle, The World Stone, Runeforged Hammer,
    Avatar''s Parashu, Dreamer''s Idol, Genji''s Guard, Breastplate of Valor, Pendulum
    Blade, Amanita Charm, Bragi''s Harp, Kinetic Cuirass, Void Shield, Deathbringer,
    Damaru, Dominance, Freya''s Tears.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.58
      pick: 0.41
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.49
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.61
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.54
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.62
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.54
      pick: 0.3
      fit: 0.72
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Tyrfing
  - Silverbranch Bow
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Nimble Ring, Berserker''s Shield, Riptalon, Tyrfing,
    Silverbranch Bow, Golden Blade, Gluttonous Grimoire, Death Metal, Soul Gem, The
    Crusher, The Reaper, Lernaean Bow, Tekko-Kagi, Toxic Blade, Spear of the Magus,
    Bragi''s Harp, Genji''s Guard, Runeforged Hammer, Breastplate of Valor, Obsidian
    Shard, Spear of Desolation, Pharaoh''s Curse, Dominance, Amanita Charm, Bracer
    of The Abyss, Kinetic Cuirass, Qin''s Blade, Shogun''s Ofuda, Freya''s Tears,
    Deathbringer, Damaru, Eye of Providence, Helm of Radiance, Demon Blade, Shield
    Splitter, Doom Orb, The Cosmic Horror.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.41
      fit: 0.31
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.55
      pick: 0.0
      fit: 0.67
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Soul Gem, Spear of
    Desolation, Genji''s Guard, Breastplate of Valor, Nimble Ring, Freya''s Tears,
    Berserker''s Shield, Death Metal, Gluttonous Grimoire, Chronos'' Pendant, The
    Crusher, Shield of the Phoenix, Spear of the Magus, Screeching Gargoyle, Silverbranch
    Bow, Obsidian Shard, Arondight, Gem of Focus, Tyrfing, The Reaper, Lernaean Bow,
    Riptalon, Golden Blade, Totem of Death, Amanita Charm, Pendulum Blade, Tekko-Kagi,
    Runeforged Hammer, Kinetic Cuirass, Bragi''s Harp, Helm of Radiance, Bracer of
    The Abyss, Chandra''s Grace, Doom Orb, The Cosmic Horror, Toxic Blade, Pharaoh''s
    Curse, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.09
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.58
      pick: 0.41
      fit: 0.54
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.58
      pick: 0.12
      fit: 0.09
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.55
      pick: 0.0
      fit: 0.22
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Berserker's Shield
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    Underrated for this god: Rod of Tahuti, Death Metal, The Crusher, Berserker''s
    Shield, Nimble Ring, Tyrfing, Golden Blade, Tekko-Kagi, Lernaean Bow, Silverbranch
    Bow, Gluttonous Grimoire, Riptalon, Soul Gem, The Reaper, Spear of the Magus,
    Runeforged Hammer, Bragi''s Harp, Spear of Desolation, Obsidian Shard, Toxic Blade,
    Dominance, Genji''s Guard, Deathbringer, Damaru, Breastplate of Valor, Amanita
    Charm, Kinetic Cuirass, Pharaoh''s Curse, Demon Blade, Shield Splitter, Bracer
    of The Abyss, Musashi''s Dual Swords, Freya''s Tears, Avenging Blade, Doom Orb,
    The Cosmic Horror, Shogun''s Ofuda, Avatar''s Parashu.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.22
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.58
      pick: 0.41
      fit: 0.43
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.55
      pick: 0.0
      fit: 0.65
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.45
    The Crusher:
      total: 0.52
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.55
      pick: 0.0
      fit: 0.23
  starter: *id001
---

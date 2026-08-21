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
  - Death Metal
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Tekko-Kagi
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
    this god: Rod of Tahuti, Death Metal, The Crusher, Berserker''s Shield, Tekko-Kagi,
    Nimble Ring, Lernaean Bow, The Reaper, Gluttonous Grimoire, Soul Gem, Tyrfing,
    Golden Blade, Bragi''s Harp, Silverbranch Bow, Spear of the Magus, Runeforged
    Hammer, Spear of Desolation, Dominance, Riptalon, Obsidian Shard, Deathbringer,
    Damaru, Demon Blade, Genji''s Guard, Breastplate of Valor, Pharaoh''s Curse, Bracer
    of The Abyss, Amanita Charm, Shield Splitter, Toxic Blade, Musashi''s Dual Swords,
    Kinetic Cuirass, Avatar''s Parashu, Doom Orb, The Cosmic Horror, Shogun''s Ofuda,
    Avenging Blade, Freya''s Tears.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.58
      pick: 0.41
      fit: 0.49
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.58
      pick: 0.12
      fit: 0.25
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.54
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
    The Crusher, Spear of the Magus, Berserker''s Shield, Obsidian Shard, Genji''s
    Guard, Bragi''s Harp, Breastplate of Valor, The Reaper, Lernaean Bow, Transcendence,
    Doom Orb, Tekko-Kagi, Runeforged Hammer, Ancient Signet, The World Stone, Helm
    of Radiance, Chronos'' Pendant, Tyrfing, Dominance, Bracer of The Abyss, The Cosmic
    Horror, Golden Blade, Ethereal Staff, Freya''s Tears, Wish-Granting Pearl, Rod
    of Asclepius, Amanita Charm, Dreamer''s Idol, Silverbranch Bow, Deathbringer,
    Kinetic Cuirass, Damaru.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.58
      pick: 0.41
      fit: 0.52
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.58
      pick: 0.12
      fit: 0.28
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.53
      pick: 0.4
      fit: 0.49
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.55
      pick: 0.0
      fit: 0.42
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
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Shield of the Phoenix,
    Soul Gem, The Reaper, Kinetic Cuirass, Ethereal Staff, Rod of Asclepius, Gluttonous
    Grimoire, Riptalon, Death Metal, Runeforged Hammer, Pharaoh''s Curse, Nimble Ring,
    The Crusher, Freya''s Tears, Genji''s Guard, Phoenix Feather, Breastplate of Valor,
    Shield Splitter, Golden Blade, Shogun''s Ofuda, Yogi''s Necklace, Chandra''s Grace,
    Eye of the Storm, Spectral Armor, Mantle Of Discord, Stone of Binding, Lernaean
    Bow, Erosion, Blood-Bound Book, Eye of Providence, Spear of the Magus, Leviathan''s
    Hide, Tekko-Kagi, Lifebinder, Draconic Scale, Avenging Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.41
      fit: 0.3
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.49
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.6
    Death Metal:
      total: 0.51
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.31
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - The Crusher
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    for this god: Rod of Tahuti, The Crusher, Gluttonous Grimoire, The Reaper, Tekko-Kagi,
    Soul Gem, Spear of the Magus, Death Metal, Spear of Desolation, Obsidian Shard,
    Silverbranch Bow, Berserker''s Shield, Riptalon, Nimble Ring, Avenging Blade,
    Lernaean Bow, Stone of Binding, Doom Orb, The Cosmic Horror, Toxic Blade, The
    World Stone, Avatar''s Parashu, Screeching Gargoyle, Dreamer''s Idol, Tyrfing,
    Runeforged Hammer, Golden Blade, Pendulum Blade, Bragi''s Harp, Genji''s Guard,
    Breastplate of Valor, Amanita Charm, Dominance, Deathbringer, Damaru, Kinetic
    Cuirass, Void Shield, Pharaoh''s Curse.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.05
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.58
      pick: 0.41
      fit: 0.61
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.58
      pick: 0.12
      fit: 0.19
    The Crusher:
      total: 0.55
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.67
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.54
      pick: 0.3
      fit: 0.77
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.55
      pick: 0.0
      fit: 0.43
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
    Death Metal, Berserker''s Shield, Gluttonous Grimoire, Chronos'' Pendant, Shield
    of the Phoenix, The Crusher, Spear of the Magus, Screeching Gargoyle, Arondight,
    Gem of Focus, Obsidian Shard, Lernaean Bow, The Reaper, Pendulum Blade, Totem
    of Death, Tekko-Kagi, Silverbranch Bow, Amanita Charm, Runeforged Hammer, Bragi''s
    Harp, Kinetic Cuirass, Tyrfing, Riptalon, Chandra''s Grace, Helm of Radiance,
    Bracer of The Abyss, Golden Blade, Doom Orb, The Cosmic Horror, Pharaoh''s Curse,
    The World Stone, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.1
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.58
      pick: 0.41
      fit: 0.59
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.58
      pick: 0.12
      fit: 0.1
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.55
      pick: 0.0
      fit: 0.24
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Tekko-Kagi
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Berserker's Shield
  - Tekko-Kagi
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
    Shield, Tekko-Kagi, Nimble Ring, Lernaean Bow, Gluttonous Grimoire, Soul Gem,
    The Reaper, Tyrfing, Golden Blade, Bragi''s Harp, Silverbranch Bow, Spear of the
    Magus, Runeforged Hammer, Spear of Desolation, Dominance, Riptalon, Obsidian Shard,
    Deathbringer, Damaru, Demon Blade, Genji''s Guard, Breastplate of Valor, Pharaoh''s
    Curse, Bracer of The Abyss, Amanita Charm, Shield Splitter, Toxic Blade, Musashi''s
    Dual Swords, Kinetic Cuirass, Avatar''s Parashu, Avenging Blade, Doom Orb, The
    Cosmic Horror, Shogun''s Ofuda, Freya''s Tears.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.58
      pick: 0.41
      fit: 0.49
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.69
    The Crusher:
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
      fit: 0.26
  starter: *id001
---
